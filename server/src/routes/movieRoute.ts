import { Router } from "express";
import {
  createMovie,
  deleteMovie,
  editMovie,
  getAllMovies,
  getMovieById,
} from "../controllers/movieController";

const router = Router();

router.get("/", getAllMovies);
router.post("/", createMovie);
router.get("/:id", getMovieById);
router.put("/:id", editMovie);
router.delete("/:id", deleteMovie);

export default router;
