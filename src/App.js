import './App.css';
import React, { useState } from "react";
import logo from './logo.png'
import { Textarea, Spacer, Button, Loading } from '@nextui-org/react';

function App() {
    const [title, setTitle] = useState('');
    const [abstract, setAbstract] = useState('');
    const [highlights, setHighlights] = useState('');
    const [loading, setLoading] = useState(false);

    const titleChangeHandler = (event) => {
        setTitle(event.target.value);
    };

    const abstractChangeHandler = (event) => {
        setAbstract(event.target.value);
    }
  const fetchData = () => {
      setLoading(true);
      const prompt = `Please generate a bullet list of highlights using Title and Abstract. Title=${title}\nAbstract=${abstract}->`;
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'api-key': 'api-key' },
          body: JSON.stringify({ prompt: prompt, "max_tokens": 512, "top_p": 0.1, "n": 2 })
      };

      fetch('https://cnhealthhack.openai.azure.com/openai/deployments/chris-test/completions?api-version=2022-12-01', requestOptions)
          .then(response => response.json())
          .then(data => {
              setLoading(false);
              setHighlights(data.choices[0].text);
          });
  }

  return (
    <div className="App">
        <div>
            <span><img alt='The Toe Dippers' width="166px" height="241px" src={logo}/></span>
        </div>
        <Textarea
            placeholder="Please enter your article title."
            value={title}
            onChange={titleChangeHandler}/>
        <Spacer y={0.5} />
        <Textarea
            placeholder="Please enter your article abstract."
            minRows={50}
            value={abstract}
            onChange={abstractChangeHandler}
        />
        <div className="button-container">
            <Button onClick={fetchData} className=".button">
                { loading ? <Loading type="points" color="currentColor" size="sm" /> : 'Generate' }
            </Button>
        </div>
        <Textarea
            readOnly
            label="article highlights"
            value={highlights}
        />
    </div>
  );
}

export default App;
