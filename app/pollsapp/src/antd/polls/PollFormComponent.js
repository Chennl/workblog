import React from 'react';
import http from '../../service/http';
import LivePreview from './LivePreview';
import { Modal,Input,  Form,Button, Select ,Card,DatePicker,message} from 'antd';
import Moment from 'moment';
import styles from './styles.less';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import { Row, Col } from 'antd';

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
 

const formItemLayoutWithOutLabel = {
    wrapperCol: {
      xs: { span: 24, offset: 0 },
      sm: { span: 20, offset: 4 },
    },
  };


function PollFormComponent(props){
    const [form] = Form.useForm();
    const [modal, contextHolder] = Modal.useModal();
    const handleOk =()=>{ console.log('ok');}
    const handleCancel =()=>{ console.log('cancel');}

    const onFinish=(values)=>{
        console.log('Success',values);
        const {title,options}=values.poll;
        var date = values.poll.close_date.toDate();
        var close_date = date.getTime() / 1000;
        props.save({title,options,close_date});
        //let {title,options,close}
    /*     let options=[...values.poll.options];
        if(values.poll.new_options){
            values.poll.new_options.map((opt,index)=>{
                if(options.find((value)=>opt===value))
                    console.log(opt);
                else
                    options.push(opt)
            });
        } */
    }
    const onPreview=()=>{
        var values = form.getFieldsValue();
        const {title,options}=values.poll;
        var date = values.poll.close_date.toDate();
        var close_date = date.getTime() / 1000;
        props.preview({title,options,close_date});
    }
    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    }
    const onDateChange=(value, dateString)=>{
        console.log('Selected Time: ', value, '  Formatted Selected Time: ', dateString);

    }
    const validateOptions=(value)=>{
        var valuesSoFar = Object.create(null);
        var array = form.getFieldValue('poll').options;
        for (var i = 0; i < array.length; ++i) {
            var val = array[i];
            if (val in valuesSoFar) {
                return true;
            }
            valuesSoFar[val] = true;
        }
        return false;
    }
 
    return(
        <Form   {...formItemLayout} form={form} requiredMark onFinish={onFinish} onFinishFailed={onFinishFailed} autoComplete="off">
                <Form.Item label='Title' rules={[{required:true,message:'Topic title is required'}]} name={['poll', 'title']} >
                <Input placeholder="Title for this topic."  autoComplete='off'/>
                </Form.Item>
                <Form.Item label='Close Date' name={['poll', 'close_date']} rules={[{required:true,message:'Close date is required!'}]}>
                    <DatePicker  showNow style={{width: '100%',}} onChange={onDateChange} />
                </Form.Item>
                <Form.List
                    name={['poll',"options"]}
                    rules={[
                    {
                        validator: async (_, options) => {
                        if (!options || options.length < 2) {
                            return Promise.reject(new Error('At least 2 options'));
                        }
                        },
                    },
                    ]}
                >
                    {(fields, { add, remove }, { errors }) => (
                    <>
                        {fields.map((field, index) => (
                        <Form.Item
                            {...(index === 0 ? formItemLayout : formItemLayoutWithOutLabel)}
                            label={index === 0 ? 'Option' : ''}
                            required={false}
                            key={field.key}
                        >
                            <Form.Item
                            {...field}
                            validateTrigger={['onChange', 'onBlur']}
                            rules={[
                                {
                                required: true,
                                whitespace: true,
                                message: "Please input option description or delete this field.",
                                },
                                ({ getFieldValue }) => ({
                                    validator(rule, value) {
                                        var valuesSoFar = Object.create(null);

                                      if (!value || !validateOptions(value)) {
                                        return Promise.resolve();
                                      }
                        
                                      return Promise.reject('You have duplicated option!');
                                    },
                                  }),
                            ]}
                            noStyle
                            >
                            <Input placeholder="Option Description" style={{ width: '60%' }} />
                            </Form.Item>
                            {fields.length > 1 ? (
                            <MinusCircleOutlined
                                className="dynamic-delete-button"
                                onClick={() => remove(field.name)}
                            />
                            ) : null}
                        </Form.Item>
                        ))}
                        <Form.Item {...formItemLayoutWithOutLabel}>
                        <Button
                            type="dashed"
                            onClick={() => add()}
                            style={{ width: '60%' }}
                            icon={<PlusOutlined />}
                        >
                            Add Option
                        </Button>
                        <Form.ErrorList errors={errors} />
                        </Form.Item>
                    </>
                    )}
                </Form.List>
                <Form.Item  {...formItemLayoutWithOutLabel} justify="center">
                    <Button type="primary" htmlType="submit" disabled={false} style={{width: '60%',}}> Save Poll</Button> 
                </Form.Item>
                <Form.Item  {...formItemLayoutWithOutLabel} justify="center">
                    <Button type="primary" style={{width: '60%',}} onClick={onPreview}> Preview </Button> 
                </Form.Item>
            </Form>
    );

} 
export default PollFormComponent;