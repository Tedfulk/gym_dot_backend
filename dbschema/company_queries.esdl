SELECT company::Company {
    id,
    name
}


SELECT company::Company {
        id,
        name,
    }
    FILTER .id = <uuid>$id


INSERT company::Company {
        name := <str>$name,
    }


UPDATE company::Company
    FILTER .id = <uuid>$id
    SET {
        name := <str>$name,
    }


DELETE company::Company
    FILTER .id = <uuid>$id