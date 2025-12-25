export default function KPI({ title, value }) {
  return (
    <div style={{ background: "#444", color: "#fff", padding: "20px", borderRadius: "8px", margin: "10px", textAlign: "center", flex: 1 }}>
      <p>{title}</p>
      <h3>{value}</h3>
    </div>
  );
}
