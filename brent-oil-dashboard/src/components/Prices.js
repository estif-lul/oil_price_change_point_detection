import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Prices() {
  const [prices, setPrices] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/v1/prices")
      .then(res => setPrices(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Brent Oil Prices</h2>
      <ul>
        {prices.map((item, index) => (
          <li key={index}>{item.Date} - ${item.Price}</li>
        ))}
      </ul>
    </div>
  );
}

export default Prices;
