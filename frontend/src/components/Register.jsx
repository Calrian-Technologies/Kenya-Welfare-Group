import React, { useState } from 'react';
import axios from 'axios';
import { FaGoogle, FaApple, FaTwitter } from 'react-icons/fa'; 
import '../index.css';

const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [nationalId, setNationalId] = useState('');
    const [county, setCounty] = useState('');
    const [country, setCountry] = useState('');

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/auth/register/', {
                email,
                password,
                first_name: firstName,
                last_name: lastName,
                phone,
                national_id: nationalId,
                county,
                country,
            });
            console.log('Registration successful:', response.data);
        } catch (error) {
            console.error('Registration error:', error);
        }
    };

    return (
        <div className="login-wrap">
            <div className="login-html">
                <input id="tab-2" type="radio" name="tab" className="sign-up" checked readOnly />
                <label htmlFor="tab-2" className="tab">Register</label>
                <div className="login-form">
                    <div className="sign-up-htm">
                        <form onSubmit={handleRegister}>
                            <div className="group">
                                <div className="row">
                                    <div className="col">
                                        <label className="label">First Name</label>
                                        <input type="text" className="input" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                                    </div>
                                    <div className="col">
                                        <label className="label">Last Name</label>
                                        <input type="text" className="input" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col">
                                        <label className="label">National ID</label>
                                        <input type="text" className="input" value={nationalId} onChange={(e) => setNationalId(e.target.value)} required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col">
                                        <label className="label">Email</label>
                                        <input type="email" className="input" value={email} onChange={(e) => setEmail(e.target.value)} required />
                                    </div>
                                    <div className="col">
                                        <label className="label">Phone</label>
                                        <input type="text" className="input" value={phone} onChange={(e) => setPhone(e.target.value)} required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col">
                                        <label className="label">Password</label>
                                        <input type="password" className="input" value={password} onChange={(e) => setPassword(e.target.value)} required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col">
                                        <label className="label">County</label>
                                        <input type="text" className="input" value={county} onChange={(e) => setCounty(e.target.value)} required />
                                    </div>
                                    <div className="col">
                                        <label className="label">Country</label>
                                        <input type="text" className="input" value={country} onChange={(e) => setCountry(e.target.value)} required />
                                    </div>
                                </div>
                                <div className="group">
                                    <button type="submit" className="button">Register</button>
                                </div>
                            </div>
                        </form>
                        <div className="hr"></div>
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
                        <div className="hr"></div>
                        <div className="foot-lnk">
                            <a href="/">Already have an account? Sign In</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Register;
