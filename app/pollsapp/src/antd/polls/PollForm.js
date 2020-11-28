import React from 'react';
import http from '../../service/http';
import LivePreview from './LivePreview';
import { Radio,Input, Modal,Form,Button, Select ,Card,DatePicker,message} from 'antd';
import Moment from 'moment';
import styles from './styles.less';
import PollFormComponent from './PollFormComponent';


//global variable to store origin url (e.g http://localhost:5000)
var origin = window.location.origin;

const formItemLayout = {
    labelCol: {
        xs: { span: 24 },
        sm: { span: 4 },
    },
    wrapperCol: {
        xs: { span: 24, offset: 0 },
        sm: { span: 20, offset: 0 },
    },
  };


const { Option } = Select;
 
  
class PollForm extends React.Component {
    formRef = React.createRef();
    constructor(props){
        super(props);
        //close poll in 24 hours
        var close_date = new Date();
        close_date.setHours(close_date.getHours() + 24);
        close_date = close_date.getTime()/1000;
        this.state = {
            title: '', 
            option: '', 
            options: [], 
            close_date: close_date, 
            all_options: [],
            visible:false,
        };

        this.handleTitleChange = this.handleTitleChange.bind(this);
        this.handleOptionChange = this.handleOptionChange.bind(this);
        this.onDateChange = this.onDateChange.bind(this);
         

    }
    componentDidMount(){
        var url = origin +"/api/polls/options";
        
        http.get(url)
        .then(response=>{
            this.setState({all_options:[...response.data]});
            console.log(response);
            //{ label, value }
        })
        .catch(error=>{
            console.error(url,error);
        });
       
        
    }
    showModal = () => {
        this.setState({
          visible: true,
        });
    };
    handleCancel=()=>{
        this.setState({
            visible: false,
          });
    }
    handleSavePoll=(data)=>{

        //console.log(this.formRef.current.getFieldValue('option'));
        //let option = this.formRef.current.getFieldValue('option');
        //update poll options and reset options to an empty string
        //var duplicate = this.state.options.indexOf(this.state.option);

        var url =  origin + '/api/polls'
        http.post(url,data)
        .then(response=>{
            //alert(response.data.message);
            Modal.success({
                title: '投票创建',
                content: `${response.data.message}`,
            });
        })
        .catch(error=>{
            console.error(error);
            let message = error;
            if(error.response)
                message =error.response.data.message;
            else if(error.request){
                message = error.request;
            }
            else{
                message = error.message;
            }
            Modal.error({
                title: '创建失败',
                content: `详情:[ ${message}]`,
            });

        });


        // console.log(data);

        // var duplicate =  this.state.options.find(item=>item.name===option)
        // if(duplicate){
        //       //message.info(`您已经选择该选项: ${this.state.option}`);
        //       Modal.warning({
        //         title: '警告',
        //         content: `该选项[ ${this.state.option}]已经存在，无须再添加!`,
        //       });
        // }
        // else{
        //     this.setState({
        //         options: this.state.options.concat({name: option}),
        //         all_options: this.state.all_options.concat({name: option}),
        //         option: '',
        //         visible:false
        //     },()=> message.info(`选项: ${this.state.option}已经添加`));
        // }
    } 
    handleLivePreview=(data)=>{
        let {title,close_date} = data;
        let options = data.options.map(option=>({name:option,vote_count:0}));
        this.setState({title,close_date,options},()=>console.log(this.state));
        
    }
    onFinishFailed=()=>{

    }
    handleOk=()=>{
        this.formRef.current.submit();
    }
    afterClose=()=>{
        this.formRef.current.resetFields();
    }

    handleOptionChange(value,item){
    //console.log('handleOptionChange',value,item)
        var option = value
        this.setState({option});
    }
    handleTitleChange(e){
        //change title as the user types
        var title = e.target.value;
        this.setState({title: title});
    }
    onDateChange(value, dateString){
        console.log('Selected Time: ', value, '  Formatted Selected Time: ', dateString);
        if(value===null) return;
        var date = value.toDate();
        // convert date to UTC timestamp in seconds
        var close_date = date.getTime() / 1000;
        console.log(close_date);
        this.formRef.current.setFieldsValue({
            close: close_date,
          });
        //antd.message.info(`您选择的日期是: ${date ? date.format('YYYY-MM-DD') : '未选择'}`);
       // this.setState({close_date: close_date})
    }




    render() {
        var all_options = this.state.all_options.map(function(option){
            return(<Option  key={option.id} value={option.name} >{option.name}</Option>)
        });
         

        var all_options_ant=[];
        this.state.all_options.forEach(e => {
            all_options_ant.push({label:e.name,value:e.name});
        });
        
        return (
        <div>
            <Card title="Create a poll">
                <PollFormComponent 
                    options={all_options_ant}
                    save={this.handleSavePoll} 
                    preview ={this.handleLivePreview}
                    showModal={this.showModal}/>
            </Card>             
             
            <br/>
            <Card title="Live Preview">
            <LivePreview title={this.state.title} options={this.state.options}/>
            </Card>
            <>
                <Button type="primary" onClick={this.showModal}>
                Open Modal
                </Button>
                <Modal
                    title="添加选项"
                    visible={this.state.visible}
                    onOk={this.handleOk}
                    onCancel={this.handleCancel}
                    maskClosable={false}
                    afterClose={this.afterClose}
                >
                <Form layout="inline" labelAlign='right' ref={this.formRef} {...formItemLayout} autoComplete='off' onFinishFailed={this.onFinishFailed}  onFinish={this.handleSavePoll}> 
                    <Form.Item label="选项描述" name='option' style={{ width: '100%' }}  rules={[{required:true,message:'Option description is required'}]}>
                        <Input  />
                    </Form.Item>  
             
                </Form>
            </Modal>
            </>
        </div>
        );
        }
}

export default PollForm;