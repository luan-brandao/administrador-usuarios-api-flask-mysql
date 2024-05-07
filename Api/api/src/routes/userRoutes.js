const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');


router.post('/login', userController.login);
router.get('/', userController.getAllUsers);
router.post('/cad', userController.createUser);
router.put('/up/:id', userController.updateUser);
router.delete('/:id', userController.deleteUser);

module.exports = router;
