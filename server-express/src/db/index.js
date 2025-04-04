import dotenv from 'dotenv'
import pg from 'pg'
dotenv.config({})

const pool = new pg.Client({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false, // Required for Neon Tech
  },
});


export default pool;