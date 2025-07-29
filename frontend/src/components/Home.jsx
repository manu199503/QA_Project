import { useState } from 'react';
import { useNavigate, Link } from "react-router-dom";
import axios from 'axios';

const Home = () => {
  const [email, setEmail] = useState('');
  const [newName, setNewName] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const navigate = useNavigate();

  const handleUpdate = async () => {
    if (!email) return alert("Please enter your email");
    try {
      const res = await axios.put('http://127.0.0.1:3001/update', {
        email,
        name: newName,
        password: newPassword
      });
      alert("Updated successfully");
      console.log(res.data);
    } catch (err) {
      console.error(err);
      alert("Update failed");
    }
  };

  const handleDelete = async () => {
    if (!email) return alert("Please enter your email to delete");
    const confirm = window.confirm("Are you sure you want to delete this account?");
    if (!confirm) return;

    try {
      const res = await axios.delete('http://127.0.0.1:3001/delete', {
        data: { email }
      });
      alert(res.data);
      navigate('/register');
    } catch (err) {
      console.error(err);
      alert("Delete failed");
    }
  };

  return (
    <div
      style={{ backgroundImage: "linear-gradient(#00d5ff,#0095ff,rgba(93,0,255,.555))" }}
      className="d-flex flex-column justify-content-center align-items-center text-center vh-100"
    >
      <h1 className="mb-4">Login Success Page</h1>

      <div style={{ width: "300px" }}>
        <input
          type="email"
          className="form-control my-2"
          placeholder="Enter your email"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <input
          type="text"
          className="form-control my-2"
          placeholder="New name (optional)"
          value={newName}
          onChange={e => setNewName(e.target.value)}
        />
        <input
          type="password"
          className="form-control my-2"
          placeholder="New password (optional)"
          value={newPassword}
          onChange={e => setNewPassword(e.target.value)}
        />
        <button className="btn btn-warning my-2 w-100" onClick={handleUpdate}>Update Info</button>
        <button className="btn btn-danger my-2 w-100" onClick={handleDelete}>Delete Account</button>
        <Link to="/login" className="btn btn-light my-3 w-100">Logout</Link>
      </div>
    </div>
  );
};

export default Home;
