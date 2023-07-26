import logo from './image/1.avif'
import './Exercise.css'

const Exercise = () => {

    const div = {
        textAlign: 'center',
    }
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };
    return (
        <div style={div}>
            <h1 style={style_header}>This is a Header</h1>
            <p className="para">This is a Paragraph</p>
            <a href="#">This is a link</a>
            <h3>This is a form:</h3>
            <form>
                <label for="name">Enter your name:</label><br /><br />
                <input type="text" />
                <button>Submit</button>
            </form>
            <h4><b>Here is an image:</b></h4>
            <img src={logo} alt="image" />
            <h3>This is a list:</h3>
            <ul style={{ listStylePosition: 'inside'}}>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>
        </div>
       

    )
}

export default Exercise;