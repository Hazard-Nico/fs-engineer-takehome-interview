"use client";

import React, { useState } from 'react';
import styles from '../components/ui/form.module.css';
import axios from 'axios';

const FormPage: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    identityNumber: '',
    email: '',
    dateOfBirth: ''
  });

  const [responseMessage, setResponseMessage] = useState('');
  const [error, setError] = useState('');
  const [darkMode, setDarkMode] = useState(false);  // Dark mode toggle

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const transformedData = {
        name: formData.name,
        identity_number: formData.identityNumber,  // Transform here
        email: formData.email,
        date_of_birth: formData.dateOfBirth
      }

      const response = await axios.post('http://localhost:5358/profile', transformedData);
      setResponseMessage(response.data.message);
      setError("");
      setFormData({
        name: '',
        identityNumber: '',
        email: '',
        dateOfBirth: ''
      });
    }
    catch (error) {
      setError("An error occurred. Please try again.");
      setResponseMessage('');
    }
  };

  return (
    <div className={darkMode ? styles.darkContainer : styles.container}>
      <div className={styles.header}>Your Details</div>
      <button onClick={() => setDarkMode(!darkMode)} className={styles.toggleButton}>
        Toggle {darkMode ? 'Light' : 'Dark'} Mode
      </button>
      <form onSubmit={handleSubmit} className={styles.form}>
        <div className={styles.formGroup}>
          <label htmlFor="name">Full Name</label>
          <input type="text" className={darkMode ? styles.darkInput : styles.input} id='name' name='name' value={formData.name} onChange={handleChange} required />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="identityNumber">Identity Number</label>
          <input type="text" className={darkMode ? styles.darkInput : styles.input} id='identityNumber' name='identityNumber' value={formData.identityNumber} onChange={handleChange} required />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="email">Email</label>
          <input type="text" className={darkMode ? styles.darkInput : styles.input} id='email' name='email' value={formData.email} onChange={handleChange} required />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="dateOfBirth">Date of Birth</label>
          <input type="date" className={darkMode ? styles.darkInput : styles.input} id='dateOfBirth' name='dateOfBirth' value={formData.dateOfBirth} onChange={handleChange} required />
        </div>
        <button type='submit' className={styles.button}>Submit</button>
      </form>
      {responseMessage && <p className={styles.successMessage}>{responseMessage}</p>}
      {error && <p className={styles.errorMessage}>{error}</p>}
    </div>
  );
};

export default FormPage;