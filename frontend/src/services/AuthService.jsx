import axios from 'axios';

//const API_URL = 'http://localhost:8000/';  
const API_URL = 'http://127.0.0.1:8000/auth/';  // Django server URL

class AuthService {
    register(username, password) {
        return axios.post(API_URL + 'register/', {
            username,
            password
        });
    }

    async login(username, password) {
        const response = await axios
            .post(API_URL + 'login/', {
                username,
                password
            });
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;
    }

    logout() {
        localStorage.removeItem('user');
    }

    getCurrentUser() {
        return JSON.parse(localStorage.getItem('user'));
    }
}

export default new AuthService();
