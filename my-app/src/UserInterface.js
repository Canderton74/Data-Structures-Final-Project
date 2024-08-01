import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Select from 'react-select';
import Papa from 'papaparse';
import './UserInterface.css';

//formatting/React knowledge based on Cole's work at Boats Group this summer as an intern
//creating the UserInterface object
const UserInterface = () => {
  const [city1, setCity1] = useState(null);
  const [city2, setCity2] = useState(null);
  const [result, setResult] = useState('');
  const [treeChoice, setTreeChoice] = useState('Red Black Tree');
  const [errors, setErrors] = useState({ city1: '', city2: '' });
  const [runTime, setRunTime] = useState('');
  const [validCities, setValidCities] = useState([]);
  const [isCalculating, setIsCalculating] = useState(false);
  const [calculationCompleted, setCalculationCompleted] = useState(false);

  // Fetch and parse CSV data from city file
  useEffect(() => {
    Papa.parse('uniqueCities.csv', {
      download: true,
      header: false,
      complete: (results) => {
        // convert the parsed data into data for the react-select component
        const cities = results.data.map(row => ({ value: row[0], label: row[0] }));
        console.log(cities);
        setValidCities(cities);
      },
      error: (error) => {
        console.error('Error fetching CSV data:', error);
      }
    });
  }, []);

  // Error handling function to catch for the errors in the 2 inputs of cities
  const validateInputs = () => {
    let valid = true;
    const newErrors = { city1: '', city2: '' };

    // Check to make sure each input has a city in it and that the city is from the list
    if (!city1) {
      newErrors.city1 = 'Input cannot be empty.';
      valid = false;
    } else if (!validCities.some(c => c.value === city1.value)) {
      newErrors.city1 = 'Input must be a valid city from the list.';
      valid = false;
    }

    if (!city2) {
      newErrors.city2 = 'Input cannot be empty.';
      valid = false;
    } else if (!validCities.some(c => c.value === city2.value)) {
      newErrors.city2 = 'Input must be a valid city from the list.';
      valid = false;
    }

    // Set the error messages and return the validity to the onClick function
    setErrors(newErrors);
    return valid;
  };

  // onClick function for when the calculate button is chosen
  const handleCalculate = async () => {
    if (validateInputs()) {
      //show the "Calculating..." text
      setIsCalculating(true);
      setCalculationCompleted(false);
      setResult('');
      setRunTime('');
      const currentStartTime = Date.now();
      try {
        // Send data to the backend
        const response = await axios.post('http://localhost:8000/api/process', {
          city1: city1.value,
          city2: city2.value,
          treeChoice
        });

        // Calculate run time to get back from backend
        const endTime = Date.now();
        const elapsed = (endTime - currentStartTime) / 1000;

        console.log('Start Time:', currentStartTime);
        console.log('End Time:', endTime);
        console.log('Elapsed Time (seconds):', elapsed);

        // Update the result box with the response from backend eventually
        setResult(`${response.data.message}`);
        setRunTime(`Run Time: ${elapsed.toFixed(4)} seconds`);
        setCalculationCompleted(true);

      } catch (error) {
        console.error('Error:', error);
        setResult('An error occurred while processing your request.');
        setRunTime('');
      } finally {
        //reset isCalculating so the "Calculating..." text disappears
        setIsCalculating(false);
      }
    }
  };


  // Setting up the organization of the page using the css file
  return (
    <div className="container">
      <h1>Route Risk</h1>
      <div className="description-box">
        <p>Enter two US cities below and choose a tree structure to find out the crash probability based on historical data for each city and national highway incidents.</p>
      </div>
      <div className="inputs-container">
        <div className="input-group left">
          <Select
            value={city1}
            onChange={setCity1}
            options={validCities}
            placeholder="Enter First City"
          />
          {errors.city1 && <p className="error-message">{errors.city1}</p>}
        </div>
        <div className="input-group right">
          <Select
            value={city2}
            onChange={setCity2}
            options={validCities}
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
      {isCalculating && <p className="calculating-message">Calculating...</p>}
      <div className="result-container">
        <div className="result-box">
          <p>{result}</p>
        </div>
        <p className="run-time">{runTime}</p>
      </div>
    </div>
  );
};

// Return the object to the app for indexing and placement into the page
export default UserInterface;
