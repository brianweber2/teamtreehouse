import { InMemoryDbService } from 'angular-in-memory-web-api';

declare var file: any;

export class InMemoryEntryService implements InMemoryDbService {
    createDb() {
        let entries = [
            {
                id: 1,
                title: 'Burning Sundown Behind Trees',
                description: 'A view of the setting sun through trees',
                photo: require('../../photos/Burning-sundown-behind-trees.jpg'),
                comments: [
                    {
                        id: 1,
                        name: 'Jane Smith',
                        comment: 'This is my favorite! I love it!'
                    }
                ]
            },
            {
                id: 2,
                title: 'Water Lilies and Algas',
                description: 'Still water with floating lilies',
                photo: require('../../photos/Water-lilies-and-algas.jpg'),
                comments: [
                    {
                        id: 2,
                        name: 'Kyle Jones',
                        comment: 'Nice!'
                    },
                    {
                        id: 3,
                        name: 'Alecia Clark',
                        comment: 'All the greens make this amazing.'
                    }
                ]
            },
            {
                id: 3,
                title: 'German Steam Engine',
                description: 'Trains at the station',
                photo: require('../../photos/German-steam-engine-No.4.jpg'),
                comments: []
            },
            {
                id: 4,
                title: 'Red Sun Stripe at Horizon',
                description: 'Green fields and a glimpse of sunlight',
                photo: require('../../photos/Red-sun-stripe-at-horizon.jpg'),
                comments: [
                    {
                        id: 4,
                        name: 'Steve Johnson',
                        comment: 'It looks like trouble is on the way.'
                    },
                    {
                        id: 5,
                        name: 'Becky M',
                        comment: 'I imagine this was a shot of a storm that just passed.'
                    }
                ]
            },
            {
                id: 5,
                title: 'Sundown Behind Fields',
                description: 'Clouds taking form at sun set',
                photo: require('../../photos/Sundown-behind-fields.jpg'),
                comments: [
                    {
                        id: 6,
                        name: 'Lisa Frank',
                        comment: 'Beautiful!'
                    }
                ]
            }
        ];
        return { entries };
    }
}
