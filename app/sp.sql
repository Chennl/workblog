USE [OE]
GO
/****** Object:  StoredProcedure [SBIPlant].[P_OE_ORM_ProductsAndTicketLimitSplitToStore]    Script Date: 10/16/2020 9:14:16 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		dongjd 2014-09-26
-- Update:		dongjd 2015-12-29
-- Description:	根据ORM黑白名单、订单上下限生成客户可售产品表HH..tblStoreProducts
--				根据ORM特殊产品、上限半箱产品、下限非受限产品生成HH..OuttblProductOrderLimit
-- =============================================
ALTER proc [SBIPlant].[P_OE_ORM_ProductsAndTicketLimitSplitToStore]
as
begin
	SET NOCOUNT ON;
	
	declare @error_message nvarchar(1000)
	
	create table #t_downlimit --下限配置
	(
		item_no int,
		trade_name varchar(100),
		sub_channel_code varchar(100),
		business_type_extens varchar(100),
		town_code varchar(100),
		del_location_code varchar(100),
		int_value int,
		call_location_code varchar(100),
		ps_route varchar(100)
	)
	
	insert into #t_downlimit(item_no, trade_name, sub_channel_code, business_type_extens, town_code, del_location_code, int_value, call_location_code, ps_route)
	select item_no, ISNULL(trade_name,''), ISNULL(sub_channel_code,''), ISNULL(business_type_extens,''), ISNULL(town_code,''),
	       ISNULL(del_location_code,''), int_value, ISNULL(call_location_code,''), ISNULL(ps_route,'')
	from
	OE.SBIPlant.OE_ProductOrderLimit with(nolock)
	where function_code = 306--下限条件列表

	
	CREATE NONCLUSTERED INDEX [IDX_#t_downlimit_cols1] ON #t_downlimit(item_no asc)
	CREATE NONCLUSTERED INDEX [IDX_#t_downlimit_cols2] ON #t_downlimit(trade_name asc)
	CREATE NONCLUSTERED INDEX [IDX_#t_downlimit_cols3] ON #t_downlimit(sub_channel_code asc)
	CREATE NONCLUSTERED INDEX [IDX_#t_downlimit_cols4] ON #t_downlimit(business_type_extens asc)
	CREATE NONCLUSTERED INDEX [IDX_#t_downlimit_cols5] ON #t_downlimit(town_code asc)
	
	
	create table #t_all_product--全厂可售产品表
	(
		ProductId varchar(100)
	)
	
	
	create table #t_prioritysell_product--白名单(优先可售卖)
	(
		StoreId nvarchar(36),
		ProductId varchar(100)
	)

	create table #t_prioritysell_product_distinct--白名单产品
	(
		ProductId varchar(100)
	)
	
	
	create table #t_cantsell_product--黑名单
	(
		StoreId nvarchar(36),
		ProductId varchar(100)
	)
	
	
	--为了提快速度，将所有客户资料插入临时表，并建索引
	create table #tblStore
	(
		StoreId nvarchar(36),
		SalesLocCd nvarchar(36),--营业所
		ExtBusinessTypeCd nvarchar(2),--客户子类型
		ChainNo nvarchar(36),--KA编号
		SubTradeChannelCd nvarchar(20),--子渠道
		DeliveryLocCd nvarchar(20),--出货工厂
		ActDeliveryLocCd nvarchar(20),--实际发货工厂
		TownCode nvarchar(10),--乡镇代码
		TopLimit331 int,--上限现金
		TopLimit332 int,--上限赊账
		LowerLimit int,--下限
		PsRoute nvarchar(4),--预销线路
		PaymentTerms nvarchar(4)--付款条件
	)
	
	insert into #tblStore(StoreId,SalesLocCd,ExtBusinessTypeCd,ChainNo,SubTradeChannelCd,DeliveryLocCd,ActDeliveryLocCd,TownCode,PsRoute)
	select cust.outlet_no,grop.location_code,grop.business_type_extens,term.trade_name,grop.trade_channel,grop.del_location_code,
		case ISNULL(grop.act_del_location_code, '') when '' then grop.del_location_code else grop.act_del_location_code end as act_del_location_code, --如果客户有实际发货工厂则取实际发货工厂,否则取出货工厂.此字段目前只供下限使用
		cust.town_code,grop.ps_route
	from
	CM.SBIPlant.CM_Customer cust with(nolock)
	LEFT JOIN CM.SBIPlant.CM_CustomerGroup grop with(nolock) on cust.outlet_no = grop.outlet_no
	LEFT JOIN CM.SBIPlant.CM_CustomerTerms term with(nolock) ON cust.outlet_no = term.outlet_no
	where cust.deletion_blocks = 1 and cust.account_group = 'Z001'
	
	CREATE NONCLUSTERED INDEX [IDX_#tblStore_cols1] ON #tblStore(StoreId ASC)
	CREATE NONCLUSTERED INDEX [IDX_#tblStore_cols2] ON #tblStore(ExtBusinessTypeCd ASC)
	CREATE NONCLUSTERED INDEX [IDX_#tblStore_cols3] ON #tblStore(StoreId ASC,SalesLocCd ASC,ExtBusinessTypeCd ASC,ChainNo ASC,SubTradeChannelCd ASC,DeliveryLocCd ASC)

	create table #tblStore1
	(
		StoreId nvarchar(36),
		PaymentTerms nvarchar(4)--付款条件
	)

	insert into #tblStore1(StoreId, PaymentTerms)
	SELECT t1.outlet_no,t3.payment_terms
    FROM [CM].[SBIPlant].[CM_CustomerPartnerFunction] t1
	inner join #tblStore t2
	on t1.outlet_no = t2.StoreId
	inner join CM.SBIPlant.CM_CustomerGroup t3
	on t1.partner_number = t3.outlet_no
	where partner_type='PY'

	update t1
	set t1.PaymentTerms = t2.PaymentTerms
	from #tblStore t1, #tblStore1 t2
	where t1.StoreId = t2.StoreId

	--全厂可售产品
	declare @products varchar(max)
	select @products = string_value from OE.SBIPlant.OE_ProductOrderLimit with(nolock) where function_code = 101
	insert into #t_all_product(ProductId)
	select distinct col  --distinct是为了防止ORM上有重复产品
	from
	OE.SBIPlant.F_Split(@products,',')
	where ISNULL(col, '') <> ''
	
	CREATE NONCLUSTERED INDEX [IDX_#t_all_product_cols1] ON #t_all_product(ProductId ASC)
	
	
	--白名单(优先可售卖)插入临时表#t_prioritysell_product
	declare @call_location_code nvarchar(max),--营业所
			@business_type_extens varchar(max),--客户子类型
			@trade_name varchar(max),--KA编号
			@sub_channel_code varchar(max),--子渠道
			@del_location_code nvarchar(max),--出货工厂
			@outlet_nos nvarchar(max),--客户编号
	        @ps_route nvarchar(max),--预销线路
	        @payment_terms nvarchar(max)--付款条件
	DECLARE CUR_ROUTE1 CURSOR KEYSET FOR 
		select call_location_code,business_type_extens,trade_name,sub_channel_code,del_location_code,outlet_nos,string_value
		from OE.SBIPlant.OE_ProductOrderLimit o with(nolock)
		where o.function_code = 103--白名单
	open CUR_ROUTE1 FETCH NEXT FROM CUR_ROUTE1 INTO @call_location_code,@business_type_extens,@trade_name,@sub_channel_code,@del_location_code,@outlet_nos,@products
	while @@FETCH_STATUS = 0
	BEGIN

		insert into #t_prioritysell_product(StoreId, ProductId)
		select distinct s.StoreId, p.col
		from 
		#tblStore s with(nolock)
		join OE.SBIPlant.F_Split(@products, ',') p on isnull(p.col,'') <> ''
		where
			(ISNULL(@call_location_code, '') = '' or s.SalesLocCd in (select col from OE.SBIPlant.F_Split(@call_location_code, ',') where isnull(col, '') <> '')) --营业所
			and (ISNULL(@business_type_extens, '') = '' or s.ExtBusinessTypeCd in (select col from OE.SBIPlant.F_Split(@business_type_extens, ',') where isnull(col, '') <> '')) --客户子类型
			and (ISNULL(@trade_name, '') = '' or s.ChainNo in (select col from OE.SBIPlant.F_Split(@trade_name, ',') where isnull(col, '') <> '')) --KA编号
			and (ISNULL(@sub_channel_code, '') = '' or s.SubTradeChannelCd in (select col from OE.SBIPlant.F_Split(@sub_channel_code, ',') where isnull(col, '') <> '')) --子渠道
			and (ISNULL(@del_location_code, '') = '' or	s.DeliveryLocCd in (select col from OE.SBIPlant.F_Split(@del_location_code, ',') where isnull(col, '') <> '')) --出货工厂
			and (ISNULL(@outlet_nos,'') = '' or s.StoreId in
				(
					select t1.col
					from OE.SBIPlant.F_Split(@outlet_nos, ',') t1
					where isnull(col,'') <> ''
				)) --客户编号
			and not exists --不要重复插入
			(
				select 1 from #t_prioritysell_product tpp
				where tpp.StoreId = s.StoreId and tpp.ProductId = p.col
			)
			and exists--在全厂可售产品中
			(
				select 1 from #t_all_product allp
				where p.col = allp.ProductId
			)
	FETCH NEXT FROM CUR_ROUTE1 INTO @call_location_code,@business_type_extens,@trade_name,@sub_channel_code,@del_location_code,@outlet_nos,@products
	end
	CLOSE CUR_ROUTE1
	DEALLOCATE CUR_ROUTE1
	
	CREATE NONCLUSTERED INDEX [IDX_#t_prioritysell_product_cols1] ON #t_prioritysell_product(StoreId ASC)
	CREATE NONCLUSTERED INDEX [IDX_#t_prioritysell_product_cols2] ON #t_prioritysell_product(ProductId ASC)
	
	
	
	--黑名单插入临时表#t_cantsell_product
	DECLARE CUR_ROUTE2 CURSOR KEYSET FOR 
		select call_location_code,business_type_extens,trade_name,sub_channel_code,del_location_code,string_value,payment_terms,ps_route
		from OE.SBIPlant.OE_ProductOrderLimit o with(nolock)
		where o.function_code = 102--黑名单
	open CUR_ROUTE2 FETCH NEXT FROM CUR_ROUTE2 INTO @call_location_code,@business_type_extens,@trade_name,@sub_channel_code,@del_location_code,@products,@payment_terms,@ps_route
	while @@FETCH_STATUS = 0
	BEGIN
		insert into #t_cantsell_product(StoreId, ProductId)
		select distinct s.StoreId, p.col
		from 
		#tblStore(nolock) s
		join OE.SBIPlant.F_Split(@products, ',') p on ISNULL(p.col, '') <> ''
		where
			(ISNULL(@call_location_code, '') = '' or s.SalesLocCd in (select col from OE.SBIPlant.F_Split(@call_location_code, ',') where isnull(col, '') <> '')) --营业所
			and (ISNULL(@business_type_extens, '') = '' or s.ExtBusinessTypeCd in (select col from OE.SBIPlant.F_Split(@business_type_extens, ',') where isnull(col, '') <> '')) --客户子类型
			and (ISNULL(@trade_name, '') = '' or s.ChainNo in (select col from OE.SBIPlant.F_Split(@trade_name, ',') where isnull(col, '') <> '')) -- KA编号
			and (ISNULL(@sub_channel_code, '') = '' or s.SubTradeChannelCd in (select col from OE.SBIPlant.F_Split(@sub_channel_code, ',') where isnull(col, '') <> '')) -- 子渠道
			and (ISNULL(@del_location_code, '') = '' or s.DeliveryLocCd in (select col from OE.SBIPlant.F_Split(@del_location_code, ',') where isnull(col, '') <> '')) --出货工厂
			and (ISNULL(@payment_terms, '') = '' or s.PaymentTerms in (select col from OE.SBIPlant.F_Split(@payment_terms, ',') where isnull(col, '') <> '')) --付款条件
			and (ISNULL(@ps_route, '') = '' or s.PsRoute in (select col from OE.SBIPlant.F_Split(@ps_route, ',') where isnull(col, '') <> '')) --预销线路
		    and not exists
			(
				select 1 from #t_cantsell_product tpp
				where tpp.StoreId = s.StoreId and tpp.ProductId = p.col
			)
			and exists--在白名单中
			(
				select 1 from #t_all_product allp
				where p.col = allp.ProductId
			)
	FETCH NEXT FROM CUR_ROUTE2 INTO @call_location_code,@business_type_extens,@trade_name,@sub_channel_code,@del_location_code,@products,@payment_terms,@ps_route
	end
	CLOSE CUR_ROUTE2
	DEALLOCATE CUR_ROUTE2
	
	--CREATE NONCLUSTERED INDEX [IDX_#t_cantsell_product_cols1] ON #t_cantsell_product(StoreId ASC)
	--CREATE NONCLUSTERED INDEX [IDX_#t_cantsell_product_cols2] ON #t_cantsell_product(ProductId ASC)
	CREATE NONCLUSTERED INDEX [IDX_#t_cantsell_product_cols1] ON #t_cantsell_product(StoreId ASC, ProductId ASC)
	
	
	
	--上限
	declare 
			@customer_type varchar(10),--客户属性
			@payment_type varchar(4),--客户类型
			@topLimit int--上限值
	DECLARE CUR_ROUTE3 CURSOR KEYSET FOR 
		select customer_type,payment_type,int_value
		from OE.SBIPlant.OE_ProductOrderLimit o with(nolock)
		where o.function_code = 203--上限
	open CUR_ROUTE3 FETCH NEXT FROM CUR_ROUTE3 INTO @customer_type,@payment_type,@topLimit
	while @@FETCH_STATUS = 0
	BEGIN
		if @payment_type = '331'--现金
		begin
			update b
			set b.TopLimit331 = @topLimit
			from #tblStore b, OE.SBIPlant.OE_BusinessTypeCustomerTypeConfig tsct with(nolock)
			where b.ExtBusinessTypeCd = tsct.business_type_extens and tsct.customer_type = @customer_type
		end
		else if @payment_type = '332'--赊账
		begin
			update b
			set b.TopLimit332 = @topLimit
			from #tblStore b, OE.SBIPlant.OE_BusinessTypeCustomerTypeConfig tsct with(nolock)
			where b.ExtBusinessTypeCd = tsct.business_type_extens and tsct.customer_type = @customer_type
		end
	
	FETCH NEXT FROM CUR_ROUTE3 INTO @customer_type,@payment_type,@topLimit
	end
	CLOSE CUR_ROUTE3
	DEALLOCATE CUR_ROUTE3
	
	
	--下限
	declare @StoreId nvarchar(36),
			@ChainNo nvarchar(36),--KA编号
			@SubTradeChannelCd nvarchar(20),--子渠道
			@ExtBusinessTypeCd nvarchar(2),--客户子类型
			@TownCode nvarchar(10),--乡镇代码
			@DelLocationCode nvarchar(20),--出货工厂
			@ActDeliveryLocCd nvarchar(20),--实际发货工厂
			@lowerLimitValue int,--下限值
	        @SalesLocCd nvarchar(36),--营业所
	        @PsRoute nvarchar(4)--预销线路
	DECLARE CUR_ROUTE4 CURSOR KEYSET FOR 
		select StoreId, ChainNo, SubTradeChannelCd, ExtBusinessTypeCd, TownCode, DeliveryLocCd, ActDeliveryLocCd,PsRoute,SalesLocCd
		from #tblStore s with(nolock)
	open CUR_ROUTE4 FETCH NEXT FROM CUR_ROUTE4 INTO @StoreId,@ChainNo,@SubTradeChannelCd,@ExtBusinessTypeCd,@TownCode,@DelLocationCode,@ActDeliveryLocCd,@PsRoute,@SalesLocCd
	while @@FETCH_STATUS = 0
	BEGIN
		
		set @lowerLimitValue = null
		
		select top 1 @lowerLimitValue = int_value
		from #t_downlimit with(nolock)
		where
			(trade_name = '' or trade_name = @ChainNo)
			and (sub_channel_code = '' or sub_channel_code = @SubTradeChannelCd)
			and (business_type_extens = '' or business_type_extens = @ExtBusinessTypeCd)
			and (town_code = '' or town_code = @TownCode)
			and (del_location_code = '' or del_location_code = @ActDeliveryLocCd) --下限,如果客户有实际发货工厂则取实际发货工厂,否则取出货工厂
		    and (isnull(call_location_code,'')='' or call_location_code = @SalesLocCd)
		    and (isnull(ps_route,'')='' or ps_route = @PsRoute)
		order by item_no asc
				
		update #tblStore
		set LowerLimit = @lowerLimitValue
		where StoreId = @StoreId
	
	FETCH NEXT FROM CUR_ROUTE4 INTO @StoreId,@ChainNo,@SubTradeChannelCd,@ExtBusinessTypeCd,@TownCode,@DelLocationCode, @ActDeliveryLocCd,@PsRoute,@SalesLocCd
	end
	CLOSE CUR_ROUTE4
	DEALLOCATE CUR_ROUTE4
	

	
	update #tblStore
	set LowerLimit = (select int_value from OE.SBIPlant.OE_ProductOrderLimit with(nolock) where function_code = 301)--下限默认值
	where LowerLimit is null




	insert into #t_prioritysell_product_distinct(ProductId)
	select distinct ProductId
	from
	#t_prioritysell_product


	CREATE NONCLUSTERED INDEX [IDX_#t_prioritysell_product_distinct_cols1] ON #t_prioritysell_product_distinct(ProductId ASC)

	
	

	--begin tran
	begin try
		--delete from OE.SBIPlant.OE_CustomerProducts
		
		
		
		delete from OE.SBIPlant.OE_CustomerProducts
		where not exists(
			select top 1 1
			from
			#tblStore t1
			where t1.StoreId = outlet_no_soldto
		)
		
		insert into OE.SBIPlant.OE_CustomerProducts(outlet_no_soldto, create_date)
		select t1.StoreId, GETDATE()
		from
		#tblStore t1
		where not exists(
			select top 1 1
			from
			OE.SBIPlant.OE_CustomerProducts t2 with(nolock)
			where t2.outlet_no_soldto = t1.StoreId
		)
		
		update t2
			set t2.article_nos = t1.ProductIds,
				t2.create_date = GETDATE()
		from OE.SBIPlant.OE_CustomerProducts t2 (nolock),
		(
			select
				p2.StoreId,
				STUFF((
					select ',' + ProductId
					from
					(
							--白名单中的一定可售
							select spp.ProductId
							from #t_prioritysell_product spp
							where spp.StoreId = p2.StoreId
				
							union -- 不要union all 因为 下面这个查询会重复
				
							--全厂可售产品中,排除别的客户的优先可售产品
							select allp.ProductId
							from
							#t_all_product allp
							where not exists --排除所有（包括别的人与自己的）优先可售产品
							(
								select top 1 1 from 
								#t_prioritysell_product_distinct tpp
								where tpp.ProductId = allp.ProductId
							)
							and not exists --排除黑名单
							(
								select top 1 1 from 
								#t_cantsell_product tpp
								where tpp.StoreId = p2.StoreId and tpp.ProductId = allp.ProductId
							)
					) p1
					for xml path('')),1,1,'') as ProductIds
			from
				#tblStore p2
		) t1
		where t1.StoreId = t2.outlet_no_soldto and isnull(t1.ProductIds,'') <> isnull(t2.article_nos, '')
		

		
		
		
		--更新客户的订单上下限
		update b
		set b.top_limit331 = a.TopLimit331,--现金
			b.top_limit332 = a.TopLimit332,--赊账
			b.lower_limit = a.LowerLimit, --下限值
			b.create_date = GETDATE()
		from OE.SBIPlant.OE_CustomerProducts b with(nolock), #tblStore a
		where a.StoreId = b.outlet_no_soldto and (
			isnull(b.top_limit331,0) <> isnull(a.TopLimit331,0) or 
			isnull(b.top_limit332,0) <> isnull(a.TopLimit332,0) or 
			isnull(b.lower_limit,0) <> isnull(a.LowerLimit,0))
		
		
				
		--commit
	end try
	begin catch
		--rollback
		
		SET @error_message=error_message()
  		RAISERROR(@error_message,11,1)
  		
	end catch
	
	
	drop table #t_downlimit
	drop table #tblStore
	drop table #t_all_product
	drop table #t_cantsell_product
	drop table #t_prioritysell_product
	drop table #t_prioritysell_product_distinct
end