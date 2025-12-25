import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import FraudAlerts from "./pages/FraudAlerts";
import Rules from "./pages/Rules";
import Users from "./pages/Users";
import Login from "./pages/Login";
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <BrowserRouter>
      <Sidebar />
      <div style={{ marginLeft: "220px", padding: "20px" }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/alerts" element={<FraudAlerts />} />
          <Route path="/rules" element={<Rules />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
