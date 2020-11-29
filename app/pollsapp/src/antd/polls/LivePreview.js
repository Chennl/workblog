import React from 'react';
import { Radio,Progress,  Form,Button, Select ,Card ,Typography,Divider} from 'antd';
import {Modal} from 'antd';
const { Title, Paragraph, Text, Link } = Typography;
var TimeLeft = {
  color: '#999',
  fontSize: '15px'
}

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

function LivePreview(props){

    const [form] = Form.useForm();
    let disabled = false;
    const onFinish=(values) =>{
      
      var valuesa = form.getFieldsValue();
      console.log(values);
        var username = localStorage.getItem('username');
        //username = username ===null?'chennl':username;
      

        if( username ===null){
          //alert('please to login before your voting!');
          Modal.warning({
            title:'投票',
            content:'please to login before your voting!'

          });
          return;
        }
 
        if(!values.option){
          //alert('please to select your option!');
          Modal.warning({
            title:'投票',
            content:'please to select your option before your voting!'
          });
          return;
        }
        
        var data = {"poll_title": props.title, "option": values.option,username};
        disabled = true;
        //calls props handler
        props.voteHandler(data);
  
        //disable the button
        //this.setState({disabled: 1});
    
    }
    let options = props.options.map((option)=>{
          if(option.name){
              // calculate progress bar percentage
              var progress = Math.round((option.vote_count / props.total_vote_count) * 100) || 0;
              return (
                  <div key={option.name}>
                    <Radio value={option.uuid}>{option.name}</Radio>
                    <Progress percent={progress}></Progress>
                  </div>
                );
          } 
  });
 
  return(
        <Card title={props.title}  type="inner">
          <Form onFinish={onFinish} form={form}>
            <Form.Item name="option">
              <Radio.Group  style={{ width: '100%',}}>
              {options}
              </Radio.Group>
          </Form.Item>
          <Form.Item {...tailLayout}>
            <Button type="primary" htmlType="submit" disabled={disabled}>
            Vote!
            </Button>
            <small> {props.total_vote_count} votes so far</small>
            <small style={TimeLeft}> | {props.close_date}</small>
          </Form.Item>
          </Form>
          
        </Card>
  );
}



export default LivePreview;