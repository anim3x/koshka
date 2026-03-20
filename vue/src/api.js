import axios from 'axios';

const api = axios.create({
    baseURL: 'https://koshka.msk.ru:8000',
    headers: {
        'Content-type': 'application/json',
    },
});

export default api;