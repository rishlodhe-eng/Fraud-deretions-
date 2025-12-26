import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <nav style={{ width: "200px", position: "fixed", height: "100%", background: "#333", color: "#fff", padding: "20px" }}>
      <h2>SentinelStream</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        <li><Link style={{ color: "#fff" }} to="/">Dashboard</Link></li>
        <li><Link style={{ color: "#fff" }} to="/alerts">Fraud Alerts</Link></li>
        <li><Link style={{ color: "#fff" }} to="/rules">Rule Management</Link></li>
        <li><Link style={{ color: "#fff" }} to="/users">User Management</Link></li>
        <li><Link style={{ color: "#fff" }} to="/login">Logout</Link></li>
      </ul>
    </nav>
  );
}
