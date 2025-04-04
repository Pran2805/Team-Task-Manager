import app from "./app.js";
import pool from "./db/index.js";

app.listen(process.env.PORT || 8000, async()=>{
    console.log("Server is running on port 8000");
    await pool.connect()
    console.log(pool.host)
})