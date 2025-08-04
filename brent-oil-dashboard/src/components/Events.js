import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Events() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/v1/events")
      .then(res => setEvents(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Major Events that could affect price </h2>
      <ul>
        {events.map((item, index) => (
          <li key={index}>{item['Start Date']} - ${item.Type} - ${item['Impact Summary']}</li>
        ))}
      </ul>
    </div>
  );
}

export default Events;
