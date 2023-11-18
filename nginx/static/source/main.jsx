import React, {useState} from "react";

export default function App() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    return (
        <div>
            <h3>{count}</h3>
            <button onClick={handleClick}>
                click me
            </button>
        </div>
    )
}
