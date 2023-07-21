import express from 'express';
const router = express.Router();
import {
    _home,
    _search, 
    _searchTitle,
    _searchCategory
} from '../controllers/posts.js';

router.get('/', _home);
router.get('/search', _search);
router.post('/search/title', _searchTitle);
router.post('/search/category', _searchCategory);

export default router;