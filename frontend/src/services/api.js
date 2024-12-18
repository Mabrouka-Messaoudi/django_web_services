import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000/';
axios.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
});