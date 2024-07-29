// creating the actual page for the user interface

import React, { useState } from 'react';
import './UserInterface.css';

//creating the UserInterface object
const UserInterface = () => {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [result, setResult] = useState('');
  const [dropdownValue, setDropdownValue] = useState('Option1');
  const [errors, setErrors] = useState({ input1: '', input2: '' });

  //error handling function to catch for the errors in the 2 inputs of cities
  const validateInputs = () => {
    let valid = true;
    const newErrors = { input1: '', input2: '' };

    //check to make sure each input has a city in it
    if (!input1.trim()) {
      newErrors.input1 = 'Input cannot be empty.';
      valid = false;
    }

    if (!input2.trim()) {
      newErrors.input2 = 'Input cannot be empty.';
      valid = false;
    }

    //make sure that only letters and spaces are in the inputs
    if (input1.trim() && /[^a-zA-Z\s]/.test(input1)) {
      newErrors.input1 = 'Input can only contain letters.';
      valid = false;
    }

    if (input2.trim() && /[^a-zA-Z\s]/.test(input2)) {
      newErrors.input2 = 'Input can only contains letters.';
      valid = false;
    }

    //set the error messages and return the validity to the onClick function
    setErrors(newErrors);
    return valid;
  };

  //onClick function for when the calculate button is chosen
  const handleCalculate = () => {
    if (validateInputs()) {
      // this is where the results will be pasted from the backend
      setResult(`Results for ${input1} to ${input2}:`);
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
            value={input1}
            onChange={(e) => setInput1(e.target.value)}
            placeholder="Enter First City"
          />
          {errors.input1 && <p className="error-message">{errors.input1}</p>}
        </div>
        <div className="input-group right">
          <input
            type="text"
            value={input2}
            onChange={(e) => setInput2(e.target.value)}
            placeholder="Enter Second City"
          />
          {errors.input2 && <p className="error-message">{errors.input2}</p>}
        </div>
      </div>
      <div className="dropdown-container">
        <select
          value={dropdownValue}
          onChange={(e) => setDropdownValue(e.target.value)}
        >
          <option value="Option1">Red Black Tree</option>
          <option value="Option2">B+ Tree</option>
        </select>
      </div>
      <button onClick={handleCalculate}>Calculate</button>
      <div className="result-container">
        <div className="result-box">
          <p>{result}</p>
        </div>
        <p className="run-time">Run Time</p>
      </div>
    </div>
  );
};

//return the object to the app for indexing and placement into the page
export default UserInterface;
