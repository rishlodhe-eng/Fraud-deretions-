import KPI from "../components/KPI";
import Table from "../components/Table";

export default function Dashboard() {
  return (
    <div style={{ marginLeft: "220px", padding: "20px" }}>
      <h1>Dashboard</h1>
      <div style={{ display: "flex", gap: "10px" }}>
        <KPI title="TPS" value="42,120" />
        <KPI title="Fraud %" value="1.92%" />
        <KPI title="Avg Latency" value="137 ms" />
        <KPI title="Blocked" value="12,431" />
      </div>
      <Table headers={["TxID", "User", "Amount", "Risk", "Status"]} />
    </div>
  );
}
