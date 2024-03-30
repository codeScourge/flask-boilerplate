import React, {useState} from "react";

export default function App() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }

    function handleDouble() {
        if (count != 0) {
            fetch("/api/double/" + count.toString(), {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => setCount(data["result"]));
        }
    }

    return (
        <div>
            <h3>{count}</h3>
            <button onClick={handleClick}>
                add one
            </button>
            <button onClick={handleDouble}>
                double
            </button>
        </div>
    )
}
