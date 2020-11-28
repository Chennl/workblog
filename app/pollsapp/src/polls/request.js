import axios from 'axios';

const accessToken = localStorage.getItem('accessToken');
let authTokenRequest;
const baseURL =  'http://localhost:3000';

var request = axios.create({
        baseURL: baseURL,
        appID: 8,
        headers: {
        version: "1.1.0",
        token: accessToken
        }});
// Add a request interceptor
request.interceptors.request.use(
    function(config) {
      // Do something before request is sent
      console.log(config);
      return config
    },
    function(error) {
      // Do something with request error
      return Promise.reject(error)
    }
  )
  
  // Add a response interceptor
request.interceptors.response.use(
    function(response) {
      // Do something with response data
      return response
    },
    function(error) {
      // Do something with response error
      if (401 === error.response.status) {
        // handle error: inform user, go to login, etc
        getAuthToken();
        } else {
            return Promise.reject(error);
        }
    }
  )
 
function getAuthToken() {
    axios.post('/polls/signin',{"username":localStorage.getItem('username'),
                                "password":localStorage.getItem('password')
                                }) 
    .then((res)=>{
        if(res.status === "success"){
            localStorage.setItem('accessToken',res.data.accessToken);
            return res.data.accessToken;
        } else {
            window.location = "/logout";
        }
    });
}
    
   

export default request;
