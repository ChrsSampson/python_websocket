import { useState } from 'react';
import { io as IO } from 'socket.io-client';
import './App.css';

function App() {
    const [connection, setConnection] = useState(false);

    // const server = 'ws://localhost:3000';

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

    return (
        <>
            <h1>Hello there</h1>
            <span>Connected: {connection ? 'yes' : 'no'}</span>
        </>
    );
}

export default App;
