LICENSE_SERVERS = [
                    { 'name': 'License Server 1', 
                      'address': 'test_server001', 
                      'managers': [('FlexLM', 27000),
                                   ('FlexLM', 27001),
                                   ('RLM', 5053),
                                  ]
                    },
                    { 'name': 'License Server 2', 
                      'address': 'test_server002', 
                      'managers': [('FlexLM', 27001)]
                    },
                    { 'name': 'License Server 3', 
                      'address': 'test_server003', 
                      'managers': [('FlexLM', 27000),
                                   ('RLM', 5053),
                                  ]
                    },
                    { 'name': 'License Server 4', 
                      'address': 'test_server004', 
                      'managers': [('FlexLM', 27001)]
                    },
                  ]