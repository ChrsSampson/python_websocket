import { useState } from 'react';
import { io as IO } from 'socket.io-client';
import './App.css';

function App() {
    const [connection, setConnection] = useState(false);
    const [message, setMessage] = useState('');

    // infers server by window.location
    const io = IO();

    io.on('connect', () => {
        setConnection(true);
    });

    io.on('disconnect', () => {
        setConnection(false);
    });

    io.on('message', (message) => {
        console.log(message);
    });

    function sendMessage(m) {
        io.emit('message', m);
        setMessage('');
    }

    return (
        <>
            <h1>Hello there</h1>
            <span>Connected: {connection ? 'yes' : 'no'}</span>
            <input
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={() => sendMessage(message)}>test msg</button>
        </>
    );
}

export default App;
