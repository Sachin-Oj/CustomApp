import React, { useState, useEffect } from 'react';

function Demo() {
    const [data, setData] = useState([{}])
    
    useEffect(() => {
        fetch('http://localhost:5000/members').then(res => {
            console.log(res)
            res.json().then(
                data => {
                    setData(data);
                    console.log(data);
                }
            )
        }  )
    }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload. This is demo !!!
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default Demo;
