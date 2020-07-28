//axios.defaults.baseURL = 'https://api.example.com';
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });
// Set config defaults when creating the instance
const instance = axios.create({
    baseURL: 'https://api.example.com'
  });
  
// Alter defaults after instance has been created
instance.defaults.headers.common['Authorization'] = AUTH_TOKEN;
  