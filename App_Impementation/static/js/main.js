// Function to get events from WWI Event Service api.


const callEventsService = async (month, day) => {
    try {
        // create HTTP request to GET /events endpoint and send request
        const response = await fetch({
            url: 'http://localhost:5100/events',
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({ month, day })
        });

        // request was successful
        if (response.status === 200) {
            // get events from response body
            const events = await response.json();
            // -- use events as data to be displayed in frontend UI --
            for (var i = 0; i < obj.length; i++) {
                console.log(obj[i].events);
            }
        };
    } catch (err) {
        console.error(err);
    };
};
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>

function getEventsList2() {

        $.ajax({
            url: "/events",
            type: "GET",
            datatype: 'JSON',
            data: JSON.stringify({'month': 10, "day": 26}),
            success: function(data) {
                console.log(typeof data);l
            }
        });
    }

getEventsList2()