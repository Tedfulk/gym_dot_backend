select Lessons {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
    }
    filter .id = <uuid>$lesson_id