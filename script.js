const ws = new WebSocket("ws://localhost:8765");

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // data = EEG 4ch の配列
    plot(data); // Plotly などで描画
};
