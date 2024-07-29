// creating the actual page for the user interface

import React, { useState } from 'react';
import axios from 'axios';
import './UserInterface.css';

//formatting/React knowledge based on Cole's work at Boats Group this summer as an intern
//creating the UserInterface object
const UserInterface = () => {
  const [city1, setCity1] = useState('');
  const [city2, setCity2] = useState('');
  const [result, setResult] = useState('');
  const [treeChoice, setTreeChoice] = useState('Red Black Tree');
  const [errors, setErrors] = useState({ city1: '', city2: '' });
  const [runTime, setRunTime] = useState('');

  //error handling function to catch for the errors in the 2 inputs of cities
  const validateInputs = () => {
    let valid = true;
    const newErrors = { city1: '', city2: '' };

    //check to make sure each input has a city in it
    if (!city1.trim()) {
      newErrors.city1 = 'Input cannot be empty.';
      valid = false;
    }

    if (!city2.trim()) {
      newErrors.city2 = 'Input cannot be empty.';
      valid = false;
    }

    //make sure that only letters and spaces are in the inputs
    if (city1.trim() && /[^a-zA-Z\s]/.test(city1)) {
      newErrors.city1 = 'Input can only contain letters.';
      valid = false;
    }

    if (city2.trim() && /[^a-zA-Z\s]/.test(city2)) {
      newErrors.city2 = 'Input can only contains letters.';
      valid = false;
    }

    //set the error messages and return the validity to the onClick function
    setErrors(newErrors);
    return valid;
  };

  //onClick function for when the calculate button is chosen
  const handleCalculate = async () => {
    if (validateInputs()) {
      const currentStartTime = Date.now();
      try {
        // Send data to the backend
        const response = await axios.post('http://localhost:8000/api/process', {
          city1,
          city2,
          treeChoice
        });

        //calculate run time to get back from backend
        const endTime = Date.now();
        const elapsed = (endTime - currentStartTime) / 1000;

        console.log('Start Time:', currentStartTime);
        console.log('End Time:', endTime);
        console.log('Elapsed Time (seconds):', elapsed);

        // update the result box with the response from backend eventually
        setResult(`${response.data.message}`);
        setRunTime(`Run Time: ${elapsed.toFixed(4)} seconds`);

      } catch (error) {
        console.error('Error:', error);
        setResult('An error occurred while processing your request.');
        setRunTime('');
      }
    }
  };

  //setting up the organization of the page using the css file
  return (
    <div className="container">
      <h1>Route Risk</h1>
      <div className="description-box">
        <p>Enter two US cities below and choose a tree structure to find out the crash probability based on historical data for each city and national highway incidents.</p>
      </div>
      <div className="inputs-container">
        <div className="input-group left">
          <input
            type="text"
            value={city1}
            onChange={(e) => setCity1(e.target.value)}
            placeholder="Enter First City"
          />
          {errors.city1 && <p className="error-message">{errors.city1}</p>}
        </div>
        <div className="input-group right">
          <input
            type="text"
            value={city2}
            onChange={(e) => setCity2(e.target.value)}
            placeholder="Enter Second City"
          />
          {errors.city2 && <p className="error-message">{errors.city2}</p>}
        </div>
      </div>
      <div className="dropdown-container">
        <select
          value={treeChoice}
          onChange={(e) => setTreeChoice(e.target.value)}
        >
          <option value="Red Black Tree">Red Black Tree</option>
          <option value="B+ Tree">B+ Tree</option>
        </select>
      </div>
      <button onClick={handleCalculate}>Calculate</button>
      <div className="result-container">
        <div className="result-box">
          <p>{result}</p>
        </div>
        <p className="run-time">{runTime}</p>
      </div>
    </div>
  );
};

//return the object to the app for indexing and placement into the page
export default UserInterface;
