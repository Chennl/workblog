import axios from 'axios'

let isDebug=true;
// 创建axios实例
const service = axios.create({
    // baseURL: process.env.BASE_API, // api 的 base_url
    timeout: 5000, // 请求超时时间
  });
  service.defaults.headers['Content-Type'] = 'application/json'; 
  service.defaults.headers['Accept'] = 'application/json';

// request拦截器
service.interceptors.request.use(
    config => {
    //   if (token_required) {
    //     config.headers['X-Token'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
    //   }
      return config
    },
    error => {
      // Do something with request error
      console.log('封装信息:',error) // for debug
      Promise.reject(error)
    }
  );
 
  // Add a response interceptor
  service.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    if(isDebug)      
    console.log('封装响应信息:',response);

    return response;
  }, function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    console.log('封装响应错误信息:',error);
    return Promise.reject(error);
  });

  export default service;
  