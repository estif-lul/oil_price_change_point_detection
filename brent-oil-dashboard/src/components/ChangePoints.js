import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ChangePoints() {
  const [change_point, setChangePoints] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/v1/change-points")
      .then(res => setChangePoints(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Change Points</h2>
      <ul>
        {change_point.map((item, index) => (
          <li key={index}>{item.tau_date} - ${item.count}</li>
        ))}
      </ul>
    </div>
  );
}

export default ChangePoints;
