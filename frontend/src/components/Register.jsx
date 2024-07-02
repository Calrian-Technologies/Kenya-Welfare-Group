
import React, { useState } from 'react';
import axios from 'axios';

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
        <form className="register-form" onSubmit={handleRegister}>
            <h2>Register</h2>
            <div className="form-row">
                <div className="form-group">
                    <label>Email:</label>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Password:</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>
            </div>
            <div className="form-row">
                <div className="form-group">
                    <label>First Name:</label>
                    <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Last Name:</label>
                    <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                </div>
            </div>
            <div className="form-row">
                <div className="form-group">
                    <label>Phone:</label>
                    <input type="text" value={phone} onChange={(e) => setPhone(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>National ID:</label>
                    <input type="text" value={nationalId} onChange={(e) => setNationalId(e.target.value)} required />
                </div>
            </div>
            <div className="form-row">
                <div className="form-group">
                    <label>County:</label>
                    <input type="text" value={county} onChange={(e) => setCounty(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Country:</label>
                    <input type="text" value={country} onChange={(e) => setCountry(e.target.value)} required />
                </div>
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
