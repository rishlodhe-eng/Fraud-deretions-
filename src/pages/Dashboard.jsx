import { useEffect, useState } from "react";

export default function Dashboard() {
  const [kpis, setKpis] = useState({});
  const [txs, setTxs] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/kpis")
      .then(res => res.json())
      .then(data => setKpis(data));

    fetch("http://127.0.0.1:8000/api/transactions")
      .then(res => res.json())
      .then(data => setTxs(data));
  }, []);

  return (
    <div>
      <h1>SentinelStream Dashboard</h1>

      <ul>
        <li>TPS: {kpis.tps}</li>
        <li>Fraud Rate: {kpis.fraud_rate}</li>
        <li>Avg Latency: {kpis.avg_latency}</li>
        <li>Blocked Tx: {kpis.blocked_tx}</li>
      </ul>

      <h2>Recent Transactions</h2>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Amount</th>
            <th>Risk</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {txs.map(tx => (
            <tr key={tx.id}>
              <td>{tx.id}</td>
              <td>{tx.user}</td>
              <td>{tx.amount}</td>
              <td>{tx.risk}</td>
              <td>{tx.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
