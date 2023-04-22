ALL_LESSONS = r"""
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
"""


CREATE_LESSON = r"""
select (
    insert Lessons {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    }
) {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
}
"""


DELETE_LESSON = r"""
delete Lessons
    filter .id = <uuid>$lesson_id
"""


GET_LESSON = r"""
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
"""


UPDATE_LESSON = r"""
select (
    update Lessons
    filter .id = <uuid>$lesson_id
    set {
        class_dates := <array<cal::local_date>>$class_dates,
        class_times := <array<cal::local_time>>$class_times,
        len_of_class_time := <int32>$len_of_class_time,
        active := <bool>$active,
        max_attendees := <int32>$max_attendees,
        min_attendees := <int32>$min_attendees,
        waitlist := <int32>$waitlist,
    }
) {
    id,
    class_dates,
    class_times,
    len_of_class_time,
    active,
    max_attendees,
    min_attendees,
    waitlist,
}
"""
