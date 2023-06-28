// Instructions
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
// Instantiate a new Video instance and call the watch() method.
// Instantiate a second Video instance with different values.
// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.

class Video{
    constructor(title, uploader, time){
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch(){
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
    }
}

const video1 = new Video('Funny pets', 'Marina', '200');
video1.watch();
const video2 = new Video('Cake recepie', 'Marina', '300');
video2.watch();


const videoData = [
    {
      title: "Funny Pets",
      uploader: "JohnDoe",
      time: 180
    },
    {
      title: "Cake Recepie",
      uploader: "MarinaR",
      time: 200
    },
    {
        title: "Travel Vlog",
        uploader: "MarkR",
        time: 600
    },
    {
        title: "ASMR",
        uploader: "Marry",
        time: 700
    },
    {
        title: "Js Lesson",
        uploader: "Hjvbkjnlml",
        time: 600
    },
  ];

// Bonus: way 1
  const videos = [];
  for (let data of videoData) {
    const video = new Video(data.title, data.uploader, data.time);
    videos.push(video);
  }

  for (let video of videos) {
    video.watch();
  }
// Bonus: way2
  const videos2 = [];
  videoData.forEach(item => videos2.push(new Video(item['title'], item['uploader'], item['time'])));
  videos2.forEach(item => item.watch());

  