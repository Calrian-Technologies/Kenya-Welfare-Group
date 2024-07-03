import React, { useState } from 'react';
import { FaGoogle, FaApple, FaTwitter } from 'react-icons/fa';
import axios from 'axios';
import '../index.css'

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/auth/login/', {
                email,
                password,
            });
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
            console.log('Login successful');
        } catch (error) {
            console.error('Login error:', error);
        }
    };

    return (
        <div className="login-wrap">
            <div className="login-html">
                <input id="tab-1" type="radio" name="tab" className="sign-in" checked readOnly />
                <label htmlFor="tab-1" className="tab">Sign In</label>
                <input id="tab-2" type="radio" name="tab" className="sign-up" readOnly />
                <label htmlFor="tab-2" className="tab"></label>
                <div className="login-form">
                    <div className="sign-in-htm">
                        <form onSubmit={handleLogin}>
                            <div className="group">
                                <label className="label">Email</label>
                                <input type="email" className="input" value={email} onChange={(e) => setEmail(e.target.value)} required />
                            </div>
                            <div className="group">
                                <label className="label">Password</label>
                                <input type="password" className="input" value={password} onChange={(e) => setPassword(e.target.value)} required />
                            </div>
                            <div className="group">
                                <button type="submit" className="button">Login</button>
                            </div>
                        </form>
                        <div className="hr"></div>
                        <div className="foot-lnk">
                            <a href="/register">Don't have an account? Register</a>
                        </div>
                        <div className="social-buttons">
                            <h3>Or Sign Up With</h3>
                            <div className="row">
                                <div className="col">
                                    <button className="social-button google">
                                        <FaGoogle className="icon" /> Google
                                    </button>
                                </div>
                                <div className="col">
                                    <button className="social-button apple">
                                        <FaApple className="icon" /> Apple
                                    </button>
                                </div>
                                <div className="col">
                                    <button className="social-button twitter">
                                        <FaTwitter className="icon" /> Twitter
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
