const cors = require('cors');
const express = require('express');
const mongoose = require('mongoose');
const FormDataModel = require('./models/FormData');

// Swagger setup
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocument = YAML.load('./swagger.yaml');

const app = express();
app.use(express.json());
app.use(cors());

// Swagger route
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/practice_mern');

// In-memory "login" tracker
let loggedInUsers = new Set();

// Register
app.post('/register', (req, res) => {
  const { email, password } = req.body;
  FormDataModel.findOne({ email }).then(user => {
    if (user) {
      res.json("Already registered");
    } else {
      FormDataModel.create(req.body)
        .then(log_reg_form => res.json(log_reg_form))
        .catch(err => res.json(err));
    }
  });
});

// Login
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  FormDataModel.findOne({ email }).then(user => {
    if (user) {
      if (user.password === password) {
        loggedInUsers.add(email);
        res.json("Success");
      } else {
        res.json("Wrong password");
      }
    } else {
      res.json("No records found!");
    }
  });
});

// Update user
app.put('/update', (req, res) => {
  const { email, name, password } = req.body;

  if (!loggedInUsers.has(email)) {
    return res.status(401).json("Unauthorized. Please login first.");
  }

  const updateData = {};
  if (name) updateData.name = name;
  if (password) updateData.password = password;

  FormDataModel.findOneAndUpdate({ email }, updateData, { new: true })
    .then(updatedUser => {
      if (!updatedUser) return res.json("User not found");
      res.json(updatedUser);
    })
    .catch(err => res.json(err));
});

// Delete user
app.delete('/delete', (req, res) => {
  const { email } = req.body;

  FormDataModel.findOneAndDelete({ email })
    .then(deletedUser => {
      if (!deletedUser) return res.json("User not found");
      loggedInUsers.delete(email);
      res.json("User deleted successfully");
    })
    .catch(err => res.json(err));
});

// Start server
app.listen(3001, () => {
  console.log("Server listening at http://127.0.0.1:3001");
  console.log("Swagger docs available at http://127.0.0.1:3001/api-docs");
});
