import React, { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import Chart from 'chart.js/auto'; // Make sure to install chart.js if you haven't

const WebcamCapture = () => {
    const webcamRef = useRef(null);
    const [processingStatus, setProcessingStatus] = useState('');
    const [results, setResults] = useState([]);

    const captureAndSend = async () => {
        const canvas = document.createElement('canvas');
        canvas.width = webcamRef.current.videoWidth;
        canvas.height = webcamRef.current.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(webcamRef.current, 0, 0);

        // Convert canvas to Blob
        canvas.toBlob(async (blob) => {
            setProcessingStatus('Processing...');
            try {
                const formData = new FormData();
                formData.append('file', blob, 'webcam-image.jpg');

                const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });

                setProcessingStatus('Processing complete.');
                updateResults(response.data); // Update results using the response from the server
            } catch (error) {
                console.error('Error uploading the file:', error);
                setProcessingStatus('Error processing image.');
            }
        }, 'image/jpeg');
    };

    const updateResults = (data) => {
        setResults(data);
        data.forEach(result => {
            if (result.type === 'fruit/vegetable') {
                updateFreshnessChart(result.metrics["Freshness Index"]);
            }
        });
    };

    const updateFreshnessChart = (freshnessIndex) => {
        const ctx = document.getElementById('freshnessChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Freshness Index'],
                datasets: [{
                    label: 'Freshness (%)',
                    data: [freshnessIndex * 100],
                    backgroundColor: ['rgba(75, 192, 192, 0.2)'],
                    borderColor: ['rgba(75, 192, 192, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    };

    useEffect(() => {
        const video = document.createElement('video');
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                video.srcObject = stream;
                video.play();
                webcamRef.current = video;
            });

        // Capture and send image every 5 seconds
        const interval = setInterval(captureAndSend, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h2>Webcam Capture</h2>
            <video ref={webcamRef} width={640} height={480} />
            <button onClick={captureAndSend}>Capture Image</button>
            <p id="processing-status">{processingStatus}</p>
            <div id="results">
                {results.map((result, index) => (
                    <div key={index}>
                        {result.type === 'fruit/vegetable' && (
                            <div className="metrics">
                                <h3>Fruit/Vegetable Metrics:</h3>
                                <p>Freshness Index: {result.metrics["Freshness Index"] * 100}%</p>
                                <p>Ripeness Stage Index: {result.metrics["Ripeness Stage Index"] * 100}%</p>
                                <p>Size Index: {result.metrics["Size Index"] * 100}%</p>
                                <p>Color Index: {result.metrics["Color Index"] * 100}%</p>
                                <p>Nutrition Index: {result.metrics["Nutrition Index"] * 100}%</p>
                                <p>Weight Index: {result.metrics["Weight Index"] * 100}%</p>
                                <p>Lifespan Score: {result.metrics["Lifespan Score"] * 100}%</p>
                            </div>
                        )}
                        {result.type === 'packaging' && (
                            <div className="product-details">
                                <h3>Packaging Item Details:</h3>
                                <p>Product Name: {result.details.product_name}</p>
                                <p>Brand: {result.details.brand}</p>
                                <p>Price: {result.details.price}</p>
                                <p>Weight: {result.details.weight}</p>
                                <p>Expire Date: {result.details.expire_date}</p>
                                <p>Ingredients: {result.details.ingredients}</p>
                            </div>
                        )}
                    </div>
                ))}
            </div>
            <canvas id="freshnessChart" width="400" height="200"></canvas>
        </div>
    );
};

export default WebcamCapture;
