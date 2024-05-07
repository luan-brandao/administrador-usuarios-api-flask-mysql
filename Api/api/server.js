const express= require('express');
const path = require('path'); 
//importando dotenv para usar variaveis de ambiente
require('dotenv').config({ path:"src/.env" }); 
//importando as rotas
const userRoutes = require('./src/routes/userRoutes');
//importando banco de dados
const ConnectMongoDB = require("./src/database");

//instanciando express para recerber  as funções do framework
const app = express();

//conectando ao banco de dados
ConnectMongoDB();

// Define o diretório de visualizações estáticas
app.use(express.static(path.join(__dirname, 'src', 'views')));

// Rota para servir o arquivo index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname,'views', 'index.html'));
});


app.use(express.json());
app.use('/api',userRoutes);

app.listen(process.env.PORT || 3000, () => {
    console.log(`Server rodando na porta: ${process.env.PORT}`);
}); 


console.log(process.env.MONGODB_URI);
console.log(process.env.PORT);