import { Component } from 'react';
import {Link} from 'react-router-dom';
import { Layout,Menu } from 'antd';
import { DashboardOutlined,PieChartOutlined,GithubOutlined} from '@ant-design/icons';
import logo from '../assets/logo.svg';

// Header, Footer, Sider, Content组件在Layout组件模块下
const { Header, Footer, Sider, Content } = Layout;

const SubMenu = Menu.SubMenu;

<DashboardOutlined style={{ fontSize: '16px', color: '#08c' }} />;
 
export default class BasicLayout extends Component {
    render() {
      return (
          <Layout>
          <Sider logo={logo}  width={256} style={{ minHeight: '100vh', color: 'white' }}>
            <div style={{height:'32px',background:'rgba(255,255,255,.2)',margin:'16px'}} />
            <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1">
              <PieChartOutlined />
              <span>Helloworld</span>
            </Menu.Item>
            <SubMenu
              key="1-1"
              title={<span><GithubOutlined style={{ fontSize: '16px', color: '#08c' }} /><span>Polls</span></span>}
            >
               <Menu.Item key="1-1-1"><Link to="/polls">Polls Station</Link></Menu.Item>
               <Menu.Item key="1-1-2"><Link to="/polls/create">Create Poll</Link></Menu.Item>
             
            </SubMenu>
            <SubMenu
              key="sub1"
              title={<span><DashboardOutlined style={{ fontSize: '16px', color: '#08c' }} /><span>Dashboard</span></span>}
            >
               <Menu.Item key="2">分析页</Menu.Item>
               <Menu.Item key="3">监控页</Menu.Item>
               <Menu.Item key="4">工作台</Menu.Item>
            </SubMenu>
          </Menu>
          </Sider>
          <Layout >
            <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>Header</Header>
            <Content style={{ margin: '24px 16px 0' }}>
              <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>
                {this.props.children}
              </div>
            </Content>
            <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
          </Layout>
        </Layout>
      )
    }
  }