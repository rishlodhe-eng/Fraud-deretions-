export default function Table({ headers = [] }) {
  return (
    <table style={{ width: "100%", borderCollapse: "collapse", marginTop: "20px" }}>
      <thead>
        <tr>
          {headers.map((h) => (
            <th key={h} style={{ border: "1px solid #ccc", padding: "10px", textAlign: "left" }}>{h}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colSpan={headers.length} style={{ padding: "10px", textAlign: "center" }}>No data yet</td>
        </tr>
      </tbody>
    </table>
  );
}
