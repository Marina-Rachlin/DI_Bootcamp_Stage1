import './App.css';
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';
import first from './images/1.jpg';
import second from './images/2.webp';
import third from './images/3.webp';
import fourth from './images/4.webp';


function App() {
  return (
    <div className='parent'>
    <Carousel>
        <div>
            <img src={first} alt='Hong Kong' />
            <p className="legend">Hong Kong</p>
        </div>
        <div>
            <img src={second} alt='Macao' />
            <p className="legend">Macao</p>
        </div>
        <div>
            <img src={third} alt='Japan' />
            <p className="legend">Japan</p>
        </div>
        <div>
            <img src={fourth} alt='New York' />
            <p className="legend">New York</p>
        </div>
    </Carousel>
    </div>
  );
}

export default App;