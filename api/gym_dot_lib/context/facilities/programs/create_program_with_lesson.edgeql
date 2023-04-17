select (
insert Programs {
    name := <str>$name,
    description := <str>$description,
    active := <bool>$active,
    lesson := {
    (insert Lessons {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    } 
    )
    }
}
) {
    id,
    name, 
    description,
    active,
    lesson: {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
    }
}