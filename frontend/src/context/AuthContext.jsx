import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Check if the user is already logged in when the app loads
        const checkUser = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/auth/user/');
                setUser(response.data);
            } catch (error) {
                setUser(null);
            } finally {
                setLoading(false);
            }
        };

        checkUser();
    }, []);

    const login = async (email, password) => {
        try {
            const response = await axios.post('http://localhost:8000/api/auth/login/', { email, password });
            setUser(response.data.user);
        } catch (error) {
            console.error('Login error:', error);
            throw error;
        }
    };

    const register = async (email, password, firstName, lastName, phone, nationalId, county, country) => {
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
            setUser(response.data.user);
        } catch (error) {
            console.error('Registration error:', error);
            throw error;
        }
    };

    const logout = async () => {
        try {
            await axios.post('http://localhost:8000/api/auth/logout/');
            setUser(null);
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    return (
        <AuthContext.Provider value={{ user, loading, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthContext;